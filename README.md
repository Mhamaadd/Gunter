# Gunter Static Website

This project contains a static website hosted on AWS S3, with automatic deployment using GitHub Actions.

## Project Contents

- HTML, CSS, and other static files organized in the project folders.
- A GitHub Actions workflow file located at `.github/workflows/deploy.yml` that handles automatic deployment to AWS S3.

## How It Works

- Whenever you push changes to the `main` branch on GitHub, the workflow is triggered.
- The workflow syncs the project files to the AWS S3 bucket hosting the static website.

## Prerequisites

- An AWS account with proper permissions to access and write to the S3 bucket.
- GitHub repository secrets configured with:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

## How to Update

1. Make your changes to the website files (e.g., `index.html`).
2. Commit and push your changes to the `main` branch.
3. GitHub Actions will automatically deploy the updated site to the S3 bucket.

## Useful Links

- [AWS S3](https://aws.amazon.com/s3/)
- [GitHub Actions](https://docs.github.com/en/actions)

## License and Credits

This website uses a template by [HTML5 UP](https://html5up.net/) under the Creative Commons Attribution 3.0 License.
---

If you have any questions or need help, feel free to reach out.
