const express = require("express");

const app = express();
const stageRoutes = require('./routes/stage.js');
const MiddlewareLogsrequest = require('./middleware/logs.js');

app.use(MiddlewareLogsrequest);
app.use(express.json());
app.use('/stage', stageRoutes);

app.get("/", (req, res) => {
    res.send("hello")
});

const PORT = 4000;
const HOST = '0.0.0.0'; // Mendengarkan pada semua interface

app.listen(PORT, HOST, () => {
    console.log(`Server berhasil di running di port ${PORT}`);
});
