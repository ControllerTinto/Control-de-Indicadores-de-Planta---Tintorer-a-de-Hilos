import os


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Falta configurar {name}")
    return value.strip()


def get_oracle_connection():
    try:
        import oracledb
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Falta instalar la dependencia 'oracledb' para consultar Oracle."
        ) from exc

    dsn = os.getenv("ORACLE_DSN")
    if not dsn:
        host = _required_env("ORACLE_HOST")
        port = int(os.getenv("ORACLE_PORT", "1521"))
        service_name = _required_env("ORACLE_SERVICE_NAME")
        dsn = oracledb.makedsn(host, port, service_name=service_name)

    return oracledb.connect(
        user=_required_env("ORACLE_USER"),
        password=_required_env("ORACLE_PASS"),
        dsn=dsn,
    )
