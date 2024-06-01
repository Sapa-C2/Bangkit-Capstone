const dbPool = require('../config/database');

const getAllUsers = () => {
    const SQLQuery = 'SELECT * FROM users';
    return dbPool.execute(SQLQuery);
    
}

const createNewUser = (body) => {
    const SQLQuery = `INSERT INTO users(name,password,email)
                      VALUES ('${body.name}','${body.password}','${body.email}')`;
                      return dbPool.execute(SQLQuery);
}

const UpdateUser = (body, idUser) => {
    const SQLQuery = `UPDATE users
                      SET name='${body.name}', password='${body.password}', email='${body.email}'
                      WHERE id ='${idUser}'`;

                      return dbPool.execute(SQLQuery);
}

const DeleteUser = (idUser) => {
    const SQLQuery = `DELETE FROM users WHERE id='${idUser}'`;

    return dbPool.execute(SQLQuery);
}

module.exports = {
    getAllUsers,
    createNewUser,
    UpdateUser,
    DeleteUser,

}