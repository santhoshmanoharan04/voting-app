const express = require("express");
const { Client } = require("pg");

const app = express();

const client = new Client({
  host: process.env.DB_HOST || "db",
  user: "postgres",
  password: "postgres",
  database: "votes",
});

client.connect();

app.get("/", async (req, res) => {
  try {
    const result = await client.query(
      "SELECT vote, COUNT(*) as count FROM votes GROUP BY vote"
    );

    let output = "<h2>Results</h2>";

    result.rows.forEach(row => {
      output += `<p>${row.vote}: ${row.count}</p>`;
    });

    res.send(output);
  } catch (err) {
    res.send("Error fetching results");
  }
});

app.listen(80, () => {
  console.log("Result app running on port 80");
});