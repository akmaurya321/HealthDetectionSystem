import sqlite3
import os

DB_PATH = './database/HealthCareAI.db'

print("=" * 60)
print("DATABASE INSPECTION")
print("=" * 60)

# Check if DB exists
if not os.path.exists(DB_PATH):
    print(f"ERROR: Database file not found at {DB_PATH}")
    exit(1)

print(f"✓ Database found: {DB_PATH}")
print(f"  Size: {os.path.getsize(DB_PATH)} bytes")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check tables
print("\n[TABLES]")
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
for table in tables:
    print(f"  - {table[0]}")

# Check USER table schema
print("\n[USER TABLE SCHEMA]")
cur.execute("PRAGMA table_info(USER)")
columns = cur.fetchall()
for col in columns:
    print(f"  {col[1]} ({col[2]})")

# Check if USER table has any data
print("\n[USER TABLE DATA]")
cur.execute("SELECT COUNT(*) FROM USER")
count = cur.fetchone()[0]
print(f"  Total records: {count}")

if count > 0:
    cur.execute("SELECT ID, NAME, EMAIL FROM USER")
    rows = cur.fetchall()
    for row in rows:
        print(f"    ID={row[0]}, NAME={row[1]}, EMAIL={row[2]}")

# Check CONTACT table
print("\n[CONTACT TABLE]")
cur.execute("SELECT COUNT(*) FROM CONTACT")
print(f"  Total records: {cur.fetchone()[0]}")

# Check NEWSLETTER table
print("\n[NEWSLETTER TABLE]")
cur.execute("SELECT COUNT(*) FROM NEWSLETTER")
print(f"  Total records: {cur.fetchone()[0]}")

# Check PATIENTS table
print("\n[PATIENTS TABLE]")
cur.execute("SELECT COUNT(*) FROM PATIENTS")
print(f"  Total records: {cur.fetchone()[0]}")

conn.close()
print("\n" + "=" * 60)
print("END INSPECTION")
print("=" * 60)
