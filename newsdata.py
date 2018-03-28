
import psycopg2

DBNAME = "news"

# Database query for the three most popular articles of all time?
articles_query = """SELECT articles.title, count(*) as num
            FROM log, articles
            WHERE log.status='200 OK'
            AND articles.slug = substr(log.path, 10)
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 3;"""

 # Database query for the most popular article authors of all time?
author_query = """
    SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 4;"""
# Database query for the days more than 1% of requests lead to errors?
error_query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

# Query data from the database, open and close the connection
def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect(dbname= DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows

# Print the top three articles of all time
def get_top_three_articles():

    # Run Query
    results = run_query(articles_query)

     # Print Results
    print('\nTop Three Articles viewed:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" ---> ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1

       

# Print the top four most popular author 
def get_top_article_authors():
   
    # Run Query
    results = run_query(author_query)

    # Print Results
    print('\nTop popular Author By Views:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" ---> ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1

# Print the days where more than 1% of requests lead to errors?
def get_days_with_errors():
    
    # Run Query
    results = run_query(error_query)

    # Print Results
    print('\nError of days with more than 1% Requests:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " ---> " + errors)
        

if __name__ == '__main__':
   get_top_three_articles()
   get_top_article_authors()
   get_days_with_errors()
