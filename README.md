# CI/CD Pipeline Demo

Learning project for GitHub Actions, PR workflows, and branch protection.

## Project Structure

```
.
├── app.py              # Simple Flask application
├── test_app.py         # Unit tests
├── requirements.txt    # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions workflow
└── README.md
```

## CI/CD Workflow

- **Lint**: flake8 for code style
- **Test**: pytest for unit tests
- **Build**: Docker image build (future)

## Branch Protection Rules

- Require PR reviews before merging
- Require status checks to pass
- No direct pushes to `main`

## How to Contribute

1. Create a feature branch: `git checkout -b feature/my-change`
2. Make your changes
3. Push and open a PR
4. Wait for CI to pass
5. Request review
6. Merge when approved
