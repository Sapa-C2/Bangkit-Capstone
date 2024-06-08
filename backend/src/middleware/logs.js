const logsRequest = (req, res, next) => {
  console.log("terjadi request ke PATH: ", req.path);
  next();
};

module.exports = logsRequest;
