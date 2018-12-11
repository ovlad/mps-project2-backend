'use strict';

const mysql = require('mysql2/promise')

class Utils extends Helper {

  async GetDb() {
    return await mysql.createConnection({

      host: "mps2db.mysql.database.azure.com",
      user: "mps2admin@mps2db",
      password: "ParolaSecure1!",
      database: "mps2project"
    });
  }

  async runSQLQuery(query) {
    let conn = await this.GetDb();

    const result = await conn.execute(query)
    conn.end()
    return result;
  }
}

module.exports = Utils
