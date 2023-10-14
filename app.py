import random
import time

from flask import Flask, current_app
from flask import g as app_ctx
from flask import jsonify, request
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.wsgi import collect_request_attributes
from opentelemetry.propagate import extract
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import (
    SpanKind,
    Status,
    StatusCode,
    get_tracer_provider,
    set_tracer_provider,
)

provider = TracerProvider(resource=Resource(attributes={SERVICE_NAME: "app"}))
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

tracer = get_tracer_provider().get_tracer(__name__)

app = Flask(__name__)


@app.post("/books/purchase")
def purchase_book():
    with tracer.start_as_current_span("purchase_book"):
        validate_book()
        try:
            order_book()
        except Exception as ex:
            trace.get_current_span().set_status(Status(StatusCode.ERROR))
            trace.get_current_span().record_exception(ex)
            return 'Failed', 408
        return 'OK', 200


def validate_book():
    with tracer.start_as_current_span("validate_book"):
        time.sleep(random.uniform(1, 100)/1000)


def order_book():
    with tracer.start_as_current_span("order_book"):
        t = random.uniform(100, 1500)
        time.sleep(t/1000)
        if t > 700:
            raise Exception("Book server is on high load! Latency: "+str(t))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
