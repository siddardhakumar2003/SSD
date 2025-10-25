import express from "express";
import { signin, signout ,signup} from "../controller/notesController.js";

const authRouter = express.Router();
authRouter.post("/signup", signup);

authRouter.post("/signin", signin);

authRouter.post("/logout", signout);

export default authRouter;;