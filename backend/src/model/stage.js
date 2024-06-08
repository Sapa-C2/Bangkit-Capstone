const dbPool = require("../config/database");

const getAllStage = () => {
  const SQLQuery = "SELECT * FROM stage";
  return dbPool.execute(SQLQuery);
};
const getDetailStage = (stage_id) => {
  const SQLQuery = "SELECT * FROM stage WHERE stage_id = ?";
  return dbPool.execute(SQLQuery, [stage_id]);
};
const getQuestionsByStageId = (stage_id) => {
  const SQLQuery = "SELECT * FROM question WHERE stage_id = ?";
  return dbPool.execute(SQLQuery, [stage_id]);
};

module.exports = {
  getAllStage,
  getDetailStage,
  getQuestionsByStageId,
};
