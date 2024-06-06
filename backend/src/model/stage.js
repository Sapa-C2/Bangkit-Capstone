const dbPool = require("../config/database");

const getAllLevel = () => {
  const SQLQuery = "SELECT * FROM stage";
  return dbPool.execute(SQLQuery);
};
const getDetailLevel = (stage_id) => {
  const SQLQuery = "SELECT * FROM level WHERE stage_id = ?";
  return dbPool.execute(SQLQuery, [stage_id]);
};

module.exports = {
  getAllLevel,
  getDetailLevel,
};
