const dbPool = require('../config/database');

const getAllUnit = () => {
    const SQLQuery = 'SELECT * FROM unit';
    return dbPool.execute(SQLQuery);
    
}

const getDetailUnit = (unit_id) => {
    const SQLQuery = 'SELECT * FROM unit WHERE unit_id = ?';
    return dbPool.execute(SQLQuery, [unit_id]);
};

module.exports = {
    getAllUnit,
    getDetailUnit
}