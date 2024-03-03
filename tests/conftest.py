import os
import sys
from typing import Any
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.asdfasdmain import app_test


def start_application():
    return app_test


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    _app = start_application()
    yield _app


# @pytest.fixture(scope="function")
# def db(app: FastAPI) -> Generator[SessionTesting, Any, None]:
#     connection = engine.connect()
#     transaction = connection.begin()
#     session = SessionTesting(bind=connection)
#     yield session
#     session.close()
#     transaction.rollback()
#     connection.close()


@pytest.fixture(scope="function")
def client(app: FastAPI, db: SessionTesting) -> Generator[TestClient, Any, None]:

    with TestClient(app) as client:
        yield client

