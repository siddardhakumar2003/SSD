import express from "express";
import cookieParser from "cookie-parser";
import {
  authenticate,
  getAllNotes,
  createNotes,
  updateNotes,
  deleteNotes,
} from "../controller/notesController.js"; // your functions from task.js

const todoRouter = express.Router();

// Parse JSON and cookies
todoRouter.use(express.json());
todoRouter.use(cookieParser());

// ------------------- Notes CRUD ------------------- //

// Apply authentication middleware to all note routes
todoRouter.use(authenticate);

// Get all notes
todoRouter.get("/", getAllNotes);

// Create a new note
todoRouter.post("/", createNotes);

// Update a note (title, content, order)
todoRouter.put("/:id", updateNotes);

// Delete a note
todoRouter.delete("/:id", deleteNotes);

export default todoRouter;
