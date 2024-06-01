const mysql = require("mysql2");

const dbPool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'yunus765',
    database: 'db_capstone',
});

module.exports = dbPool.promise();