## To-Do List API

### Overview
Bu loyiha FastAPI yordamida yaratilgan To-Do List API hisoblanadi. API yordamida foydalanuvchilar o‘z to-do ro‘yxatlarini yaratish, o‘zgartirish va o‘chirishlari mumkin. 

### Texnologiyalar
- **FastAPI** - Asinxron va tez ishlovchi web-framework.
- **SQLAlchemy** - ORM (Object-Relational Mapping) kutubxonasi.
- **SQLite** - Ma'lumotlar bazasi.
- **Uvicorn** - ASGI serveri.
- **Alembic** - Ma'lumotlar bazasining migratsiya vositasi.

---

### Setup

#### 1. Muhitni o‘rnatish

- Avvalo, virtual muhit yaratish:
  ```bash
  python3 -m venv venv
  ```

- Virtual muhitni faollashtirish:
  ```bash
  source venv/bin/activate  # Linux/Mac
  .\venv\Scripts\activate   # Windows
  ```

- Kerakli kutubxonalarni o‘rnatish:
  ```bash
  pip install -r requirements.txt
  ```

#### 2. Ma'lumotlar bazasini sozlash

- `app/db/database.py` faylida SQLite ma'lumotlar bazasi sozlangan. FastAPI ushbu faylni ishlatadi.

---

### API Marshrutlari

- **GET /todos** - Barcha to-do ro‘yxatini ko‘rsatish.
- **POST /todos** - Yangi to-do qo‘shish.
- **GET /todos/{todo_id}** - To-do id si bo‘yicha to‘liq ma'lumotni olish.
- **PUT /todos/{todo_id}** - To-do ni yangilash.
- **DELETE /todos/{todo_id}** - To-do ni o‘chirish.

---

### Ma'lumotlar Bazasi Migratsiyalari

#### 1. Migratsiyani yaratish

Agar siz ma'lumotlar bazasi sxemasini o‘zgartirsangiz, yangi migratsiya yaratishingiz kerak bo‘ladi. Buning uchun quyidagi komandani bajarishingiz kerak:

```bash
alembic revision --autogenerate -m "Message describing the migration"
```

Bu komandadan so‘ng Alembic yangi migratsiya faylini yaratadi va uni `migrations/versions` papkasi ichiga joylashtiradi.

#### 2. Migratsiyani qo‘llash

Yaratilgan migratsiyalarni ma'lumotlar bazasiga qo‘llash uchun quyidagi komandani bajarish kerak:

```bash
alembic upgrade head
```

Bu komandadan so‘ng barcha migratsiyalar amalga oshiriladi va sizning ma'lumotlar bazangiz yangilanadi.

#### 3. Migratsiyani qaytarish

Agar ma'lumotlar bazasi o‘zgarishlarini qaytarishni istasangiz, quyidagi komandani ishlatishingiz mumkin:

```bash
alembic downgrade -1
```

Bu komandadan so‘ng oxirgi migratsiya o‘chiriladi.

#### 4. Migratsiya tarixini tekshirish

Ma'lumotlar bazasidagi migratsiya tarixini ko‘rish uchun quyidagi komandani ishlating:

```bash
alembic history --verbose
```

Bu komandadan ma'lumotlar bazasidagi barcha migratsiyalarni ko‘rishingiz mumkin.

---

### Yaratilgan API-ni ishga tushirish

FastAPI dasturini ishga tushurish uchun quyidagi komandani bajarish kerak:

```bash

uvicorn app.main:app --log-config app/core/logging.conf --reload --workers 4 --timeout-keep-alive 60

```

Docker yordamida ishga tushirish uchun quyidagi komandani bajarishingiz mumkin:

```bash
docker-compose -f docker-compose.dev.yml up --build --remove-orphans
```

Bu komanda yordamida FastAPI serveri ishga tushadi va siz API-ni `http://127.0.0.1:8000` manzilida ishlatishingiz mumkin.


