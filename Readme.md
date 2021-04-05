# Minimal Test Setup

Referral: https://github.com/benoitc/gunicorn/issues/2551

This minimal setup demonstrates a changed behavior of gunicorn's `print_config` option.

With gunicorn v20.0.4 the config is printed and the server starts.

Try this with:
```bash
docker run --rm -p '5000:5000' wjentner/gunicorn-test:20.0.4
```

With gunicorn v20.1.0 the config is printed and the process exits.

Try with:
```bash
docker run --rm -p '5000:5000' wjentner/gunicorn-test:20.1.0
```