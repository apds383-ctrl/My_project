"""Итоговый вариант приложения для преподавателя и сверки."""

import os

from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI(title="Наш первый сервис")
load_dotenv()


@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "студент"):
    return {"message": f"Привет, {name}!"}


@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Учебный сервис")
    app_author = os.getenv("APP_AUTHOR", "Не указан")

    return {
        "app_name": app_name,
        "author": app_author,
    }

@app.get("/books")
def get_books():
    return ["Введение в алгоритмы", "Чистый код", "Грокаем алгоритмы"]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    books = ["Введение в алгоритмы", "Чистый код", "Грокаем алгоритмы"]
    if 1 <= book_id <= len(books):
        return books[book_id - 1]
    return "Книга не найдена"

