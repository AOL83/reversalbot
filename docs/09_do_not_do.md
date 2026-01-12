# Do Not Do

Stage 1 has hard boundaries. These anti-patterns should be avoided.

## Anti-patterns

- **Placing live trades**: Stage 1 is mock-only.
- **Bypassing risk controls**: Risk checks must remain mandatory.
- **Using unvalidated configuration**: Always load config through the validated
  loader.
- **Reusing idempotency keys across different orders**: This can suppress
  legitimate orders.
- **Ignoring anomalies**: Anomalous data should halt execution and alert.
