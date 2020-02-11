from config.settings import DATABASE_FILE_FULL_PATH

def write(content, databaseAdapter):
    path = DATABASE_FILE_FULL_PATH
    createTableScript = "\
        CREATE TABLE IF NOT EXISTS social_media(\
            id VARCHAR(20),\
            track_name VARCHAR(100),\
            n_citacoes UNSIGNED INT,\
            size_bytes VARCHAR(20),\
            price DOUBLE,\
            prime_genre VARCHAR(20)\
        )"

    databaseAdapter.execute(path, createTableScript)  

    insertScript = "\
        INSERT INTO social_media(id, track_name, n_citacoes, size_bytes, price, prime_genre)\
        VALUES(:id, :track_name, :n_citacoes, :size_bytes, :price, :prime_genre)"

    for row in content:
        parameters = [r for r in row.values()]
        databaseAdapter.execute(path, insertScript, parameters) 


    