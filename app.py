import os
from flask import Flask, render_template, request
import pymysql
from dotenv import load_dotenv

# Local development ke liye .env load karega
load_dotenv()

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', 26713)), # Aapka port 26713 hai
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor,
        ssl={'ssl': {}} # Aiven ke liye ye line compulsory hai
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    category_total = None
    overall_total = None
    error = None
    success = None

    if request.method == 'POST':
        # 🔹 ADD EXPENSE
        if 'amount' in request.form:
            amount = request.form.get('amount')
            category = request.form.get('category')
            note = request.form.get('note')

            if not amount or not category:
                error = "Amount and Category are required"
            elif not amount.isdigit() or int(amount) <= 0:
                error = "Amount must be a positive number"
            else:
                conn = get_db()
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO expenses (amount, category, note) VALUES (%s, %s, %s)",
                    (amount, category, note)
                )
                conn.commit()
                cur.close()
                conn.close()
                success = "Expense added successfully"

        # 🔹 CATEGORY TOTAL
        if 'search_category' in request.form:
            search_category = request.form.get('search_category')
            conn = get_db()
            cur = conn.cursor()
            cur.execute(
                "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE category=%s",
                (search_category,)
            )
            category_total = cur.fetchone()['total']
            cur.close()
            conn.close()

        # 🔹 OVERALL TOTAL
        if 'overall_total' in request.form:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT COALESCE(SUM(amount), 0) AS total FROM expenses")
            overall_total = cur.fetchone()['total']
            cur.close()
            conn.close()

        # 🔹 DELETE
        if 'delete_id' in request.form:
            delete_id = request.form.get('delete_id')
            conn = get_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM expenses WHERE id=%s", (delete_id,))
            conn.commit()
            cur.close()
            conn.close()

    # FETCH ALL (Hamesha latest data dikhane ke liye)
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, amount, category, note FROM expenses")
    expenses = cur.fetchall()
    cur.close()
    conn.close()

    return render_template(
        'index.html',
        expenses=expenses,
        category_total=category_total,
        overall_total=overall_total,
        error=error,
        success=success
    )

if __name__ == '__main__':
    # Cloud environments port dynamic dete hain, isliye port=5000 default rakha hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
