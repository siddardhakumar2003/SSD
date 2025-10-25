import express from "express";
import dotenv from "dotenv";
import todoRouter from "./routes/notesRouter.js";
import authRouter from "./routes/authRouter.js";
import cors from "cors";
import cookieParser from "cookie-parser";
import { connectDB } from "./controller/notesController.js";

dotenv.config();

const app = express();

// Middleware
app.use(cors({ origin: "http://localhost:3000", credentials: true }));

app.use(express.json());

app.use(cookieParser());

let isDbConnected = false;

(async () => {
  try {
    const PORT = process.env.PORT || 5001;
    await connectDB();
    if (process.env.NODE_ENV !== "test") {
      app.listen(PORT, () => {
        console.log("Server started on PORT:", PORT);
      });
    }
  } catch (err) {
    console.error("Failed to connect to the database or start the server:", err);
    process.exit(1);
  }
})();// mount router at /todos

app.use(authRouter);
app.use("/todos", todoRouter); 

export default app;
