import argparse

from .interfaces.database import fetch
from .interfaces.file import load
from .parsers import parse_json_file


def _execute_transfer_operation(args) -> None:
    source_parameters = parse_json_file(args.source)
    destination_parameters = parse_json_file(args.destination)
    query = args.query
    batch_size = 100
    batch_iterator = fetch(source_parameters, query, batch_size)
    load(**destination_parameters, batch_iterator=batch_iterator)


def main():
    parser = argparse.ArgumentParser(description="ByteBridge CLI")
    subparsers = parser.add_subparsers(dest="operation", title="Operations")

    transfer_parser = subparsers.add_parser("transfer", help="Transfer data operation")
    transfer_parser.add_argument("--source", required=True, help="Source parameters")
    transfer_parser.add_argument(
        "--destination",
        required=True,
        help="Destination parameters",
    )
    transfer_parser.add_argument(
        "--query",
        required=True,
        help="The query to be used to fetch data from the source.",
    )
    args = parser.parse_args()

    if args.operation == "transfer":
        _execute_transfer_operation(args)


if __name__ == "__main__":
    main()
