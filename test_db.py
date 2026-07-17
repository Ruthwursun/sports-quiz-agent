from src.database import setup_and_populate_db, query_historic_facts

setup_and_populate_db()

results = query_historic_facts(
    sport="Football",
    query_text="Football World Cup history"
)

print(results)