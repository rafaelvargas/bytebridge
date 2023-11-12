import argparse

from .operations.transfer import transfer
from .parsers import parse_json_file


def _execute_transfer_operation(args: argparse.Namespace) -> None:
    source_parameters = parse_json_file(args.source)
    destination_parameters = parse_json_file(args.destination)
    source_object = args.source_object
    query = args.query
    target = args.target
    batch_size = args.batch_size
    transfer(
        source_parameters=source_parameters,
        source_object=source_object,
        query=query,
        destination_parameters=destination_parameters,
        target=target,
        batch_size=batch_size,
    )


def main():
    parser = argparse.ArgumentParser(description="ByteBridge CLI")
    subparsers = parser.add_subparsers(dest="operation", title="Operations")

    transfer_parser = subparsers.add_parser("transfer", help="Transfer data operation")
    transfer_parser.add_argument("--source", required=True, help="Source parameters")
    transfer_parser.add_argument(
        "--query",
        required=False,
        help="The query to be used to fetch data from the source.",
    )
    transfer_parser.add_argument(
        "--source-object",
        required=False,
        help="The object from the source (table name or filepath) used to extract data.",
    )
    transfer_parser.add_argument(
        "--destination",
        required=True,
        help="Destination parameters",
    )
    transfer_parser.add_argument(
        "--target",
        required=True,
        help="The target of the destination (can be a table or a filepath)",
    )
    transfer_parser.add_argument(
        "--batch-size",
        required=False,
        default=100,
        help="The target of the destination (can be a table or a filepath)",
    )
    args = parser.parse_args()

    if args.operation == "transfer":
        _execute_transfer_operation(args)


if __name__ == "__main__":
    main()
