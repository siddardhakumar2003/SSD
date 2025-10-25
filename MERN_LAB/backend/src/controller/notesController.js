import { v4 as uuidv4 } from "uuid";
import { MongoClient } from "mongodb";
import dotenv from "dotenv";
import cookieParser from "cookie-parser";
import jwt from "jsonwebtoken";

dotenv.config({ path: '../.env' });
const uri = "mongodb://127.0.0.1:27017/local"

let client;
let notesCollection;
let isConnected = false;

if (!uri) {
  console.error("MongoDB URI not found. Please set MONGODB_URI in your .env file.");
  process.exit(1);
}

export async function connectDB() {
  if (!isConnected) {
    client = new MongoClient(uri);
    try {
      await client.connect();
      const db = client.db();
      notesCollection = db.collection("notes");
      isConnected = true;
      console.log("Connected to MongoDB!");
    } catch (error) {
      console.error("Error connecting to MongoDB:", error);
      process.exit(1);
    }
  }
}

export async function closeDB() {
  if (client) {
    await client.close();
    console.log("MongoDB connection closed.");
  }
}

// ------------------ Authentication ------------------ //

export async function signup(req, res) {
  const { email, password } = req.body;
  if (!email || !password) return res.status(400).json({ error: "Missing credentials" });

  const db = client.db();
  const usersCollection = db.collection("users");

  const existingUser = await usersCollection.findOne({ email });
  if (existingUser) {
    return res.status(409).json({ error: "User already exists" });
  }

  const newUser = { email, password };
  await usersCollection.insertOne(newUser);

  const token = jwt.sign({ email }, "supersecretjwtkey123", { expiresIn: "1h" });
  res.cookie("token", token, { httpOnly: true });
  res.status(201).json({ token });
}

export async function signin(req, res) {
  const { email, password } = req.body;
  if (!email || !password) return res.status(400).json({ error: "Missing credentials" });

  const user = await client.db().collection("users").findOne({ email });
  if (!user || user.password !== password) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  const token = jwt.sign({ email }, "supersecretjwtkey123", { expiresIn: "1h" });
  res.cookie("token", token, { httpOnly: true });
  res.json({ token });
}

export async function signout(req, res) {
  res.clearCookie("token");
  res.json({});
}

export function authenticate(req, res, next) {
  const token = req.cookies.token;
  if (!token) return res.status(401).json({ error: "Unauthorized" });

  try {
    const decoded = jwt.verify(token, "supersecretjwtkey123");
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ error: "Invalid token" });
  }
}

// ------------------ Notes CRUD ------------------ //

export async function getAllNotes(req, res) {
  try {
    const allNotes = await notesCollection
      .find({ user: req.user.email })
      .sort({ order: 1 })
      .toArray();
    // Return only { id, title } to match convention
    res.status(200).json(allNotes.map(n => ({ id: n.id, title: n.title })));
  } catch (error) {
    res.status(500).json({ error: "Failed to retrieve notes" });
  }
}

export async function createNotes(req, res) {
  const { title, content = "" } = req.body; 
  if (!title) return res.status(400).json({ error: "Title required" });

  try {
    const count = await notesCollection.countDocuments({ user: req.user.email });

    const note = { 
      id: uuidv4(), 
      title, 
      content, 
      order: count,
      user: req.user.email
    };

    await notesCollection.insertOne(note);
    // Return only { id, title } to match convention
    res.status(201).json({ id: note.id, title: note.title });
  } catch (error) {
    res.status(500).json({ error: "Failed to create note" });
  }
}

export async function updateNotes(req, res) {
  const { id } = req.params;
  const { title, content = "", order } = req.body;

  if (!title) return res.status(400).json({ error: "Title required" });

  try {
    const updateData = { title, content };
    if (order !== undefined) updateData.order = order;

    const result = await notesCollection.updateOne(
      { id, user: req.user.email },
      { $set: updateData }
    );

    if (result.matchedCount === 0) return res.status(404).json({ error: "Note not found" });

    const updatedNote = await notesCollection.findOne({ id, user: req.user.email });
    res.status(200).json(updatedNote);
  } catch (error) {
    res.status(500).json({ error: "Failed to update note" });
  }
}

export async function deleteNotes(req, res) {
  const { id } = req.params;
  
  try {
    const deletedNote = await notesCollection.findOne({ id, user: req.user.email });
    if (!deletedNote) return res.status(404).json({ error: "Note not found" });

    await notesCollection.deleteOne({ id, user: req.user.email });
    // Return {} to match convention
    res.status(200).json({});
  } catch (error) {
    res.status(500).json({ error: "Failed to delete note" });
  }
}

export async function reorderNotes(req, res) {
  const { tasks } = req.body; 

  if (!Array.isArray(tasks)) return res.status(400).json({ error: "Tasks array required" });

  try {
    await Promise.all(
      tasks.map((t) =>
        notesCollection.updateOne({ id: t.id, user: req.user.email }, { $set: { order: t.order } })
      )
    );
    res.status(200).json({ success: true });
  } catch (error) {
    res.status(500).json({ error: "Failed to reorder notes" });
  }
}

export function resetNotes() {
  try {
    if (notesCollection) {
      notesCollection.deleteMany({});
      console.log("All notes deleted from database.");
    }
  } catch (error) {
    console.error("Failed to reset notes:", error);
  }
}
