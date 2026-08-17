from config.config import (
    PROJECT_ROOT,
    RAW_DATA_DIR,
    BRONZE_DATA_DIR,
    SILVER_DATA_DIR,
    GOLD_DATA_DIR,
)


def main():
    print("E-Commerce Data Engineering Pipeline")
    print("--------------------------------------")

    print(f"Project root : {PROJECT_ROOT}")
    print(f"Raw data     : {RAW_DATA_DIR}")
    print(f"Bronze data  : {BRONZE_DATA_DIR}")
    print(f"Silver data  : {SILVER_DATA_DIR}")
    print(f"Gold data    : {GOLD_DATA_DIR}")

    print("\nEnvironment setup successful!")


if __name__ == "__main__":
    main()