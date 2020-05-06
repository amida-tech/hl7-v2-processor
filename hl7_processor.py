#!/usr/bin/env python

import json
from hl7_utils import hl7_str_to_dict
from kafka import KafkaConsumer, KafkaProducer
from util.actuator import HttpHealthServer
from util.arguments import get_kafka_brokers, get_input_channel, get_output_channel

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_brokers()])

HttpHealthServer.run_thread()

while True:
    for payload in consumer:
        if payload.value is not None:
            content = str(payload.value)

            # Convert it
            input_dict = hl7_str_to_dict(content)

            # Send to output channel
            producer.send(get_output_channel(), json.loads(input_dict, indent=2))
