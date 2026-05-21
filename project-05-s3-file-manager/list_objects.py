import boto3
from datetime import timezone


def list_bucket_objects(bucket_name: str) -> None:
    """
    Audits an S3 bucket and prints every object with its
    storage class, size, and last modified timestamp.

    Usage:
        python list_objects.py
    Requires:
        - boto3 installed: pip install boto3
        - AWS CLI configured: aws configure
        - IAM permissions: s3:ListBucket on the target bucket
    """
    s3 = boto3.client("s3", region_name="eu-west-2")

    print(f"\n{'='*80}")
    print(f"  S3 Object Audit — Bucket: {bucket_name}")
    print(f"{'='*80}")
    print(f"{'Object Key':<45} {'Storage Class':<22} {'Size (KB)':<12} {'Last Modified'}")
    print(f"{'-'*45} {'-'*22} {'-'*12} {'-'*25}")

    try:
        paginator = s3.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=bucket_name)

        total_objects = 0
        total_bytes = 0

        for page in pages:
            contents = page.get("Contents", [])
            if not contents:
                print("  (bucket is empty)")
                break

            for obj in contents:
                key = obj["Key"]
                storage_class = obj.get("StorageClass", "STANDARD")
                size_kb = obj["Size"] / 1024
                last_modified = obj["LastModified"].astimezone(timezone.utc).strftime(
                    "%Y-%m-%d %H:%M UTC"
                )
                display_key = key if len(key) <= 44 else key[:41] + "..."
                print(
                    f"{display_key:<45} {storage_class:<22} {size_kb:<12.2f} {last_modified}"
                )
                total_objects += 1
                total_bytes += obj["Size"]

        print(f"\n{'='*80}")
        print(
            f"  Summary: {total_objects} objects | "
            f"Total size: {total_bytes / 1024:.2f} KB "
            f"({total_bytes / (1024*1024):.4f} MB)"
        )
        print(f"{'='*80}\n")

    except s3.exceptions.NoSuchBucket:
        print(f"\nERROR: Bucket '{bucket_name}' does not exist or is in a different region.")
    except Exception as e:
        error_code = getattr(e, "response", {}).get("Error", {}).get("Code", "")
        if error_code == "AccessDenied":
            print("\nERROR: Access denied. Check your IAM permissions for s3:ListBucket.")
        else:
            print(f"\nERROR: {e}")


if __name__ == "__main__":
    # Replace with your actual bucket name
    BUCKET_NAME = "hasan-s3-lifecycle-demo-2026"
    list_bucket_objects(BUCKET_NAME)