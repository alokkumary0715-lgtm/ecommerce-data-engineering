from pathlib import Path

from csv_ingestion import ingest_csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze"


FILES_TO_INGEST = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv",
    "payments.csv",
]


def main():

    print("Starting ingestion pipeline...")
    print("--------------------------------")

    total_records = 0

    for file_name in FILES_TO_INGEST:

        source_file = RAW_DIR / file_name

        records = ingest_csv(
            source_file,
            BRONZE_DIR,
        )

        total_records += records

    print("--------------------------------")
    print("Ingestion completed successfully.")
    print(f"Total records ingested: {total_records}")


if __name__ == "__main__":
    main()