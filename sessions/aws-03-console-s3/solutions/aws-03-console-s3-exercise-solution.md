
# AWS S3

S3 has a wide range of features, it isn't _just_ for storing objects.

## Part - 1 Dealing with files

1. Log depending on your AWS login method:
    - `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`
1. Using the CLI, create two S3 buckets (bucket names are globally unique, so if someone in the world already created a bucket called Test123, you will not be able to use it)

    ```sh
    aws s3 mb s3://yourname-bucket --profile my-profile-name
    aws s3 mb s3://yourname-bucket-2 --profile my-profile-name
    ```

1. Upload a handful of files of your choosing to the first one (make sure there is no personal information in them). Use this command while in a terminal in the `aws/handouts` folder:

    ```sh
    aws s3 cp index.html s3://yourname-bucket --profile my-profile-name
    aws s3 cp error.html s3://yourname-bucket --profile my-profile-name
    ```

1. List your buckets

    ```sh
    aws s3 ls --profile my-profile-name
    ```

1. List the files in your first bucket

    ```sh
    aws s3 ls s3://yourname-bucket --profile my-profile-name
    ```

1. Copy a file from the first to second bucket

    ```sh
    aws s3 cp s3://yourname-bucket/index.html s3://yourname-bucket-2 --profile my-profile-name
    ```

1. Move a file from the first to second bucket

    ```sh
    aws s3 mv s3://yourname-bucket/error.html s3://yourname-bucket-2 --profile my-profile-name
    ```

1. Delete a file from either bucket

    ```sh
    aws s3 rm s3://yourname-bucket-2/index.html --profile my-profile-name
    ```
