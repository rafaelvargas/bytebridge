import argparse


def _execute_transfer_operation(args) -> None:
    print("The named arguments were:", args)


def main():
    parser = argparse.ArgumentParser(description="ByteBridge CLI")
    subparsers = parser.add_subparsers(dest="operation", title="Operations")

    transfer_parser = subparsers.add_parser("transfer", help="Transfer data operation")
    transfer_parser.add_argument("--source", required=True, help="Source data location")
    transfer_parser.add_argument(
        "--destination",
        required=True,
        help="Destination data location",
    )
    transfer_parser.add_argument(
        "--query",
        required=True,
        help="Transformation query or script",
    )
    transfer_parser.add_argument("--map", required=True, help="Column mapping")

    args = parser.parse_args()

    if args.operation == "transfer":
        _execute_transfer_operation(args)


if __name__ == "__main__":
    main()
