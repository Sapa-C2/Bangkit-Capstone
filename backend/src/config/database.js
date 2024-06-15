const mysql = require("mysql2");

const dbPool = mysql.createPool({
    host: '34.101.193.90',
    user: 'root',
    password: '1234',
    database: 'db-capstone',
});
module.exports = dbPool.promise();