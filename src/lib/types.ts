export type Difficulty = "facile" | "moyen" | "challenge";

export type PlayerStatus = "waiting" | "playing" | "finished";

export interface Game {
  slug: string;
  name: string;
  description: string;
  emoji: string;
  color: string;
  isActive: boolean;
  /** Nombre de questions servies par partie, reglable depuis /admin. */
  questionsPerSession: number;
  /** Nombre de questions disponibles dans la banque pour cette categorie. */
  questionCount: number;
}

/** Question complete, telle qu'elle est stockee cote serveur. Ne quitte JAMAIS le serveur. */
export interface Question {
  id: string;
  gameSlug: string;
  difficulty: Difficulty;
  question: string;
  options: { A: string; B: string; C: string; D: string };
  correctAnswer: Letter;
  points: number;
  timeLimit: number;
  explanation: string;
  tags: string;
}

/** Version envoyee au navigateur : sans la bonne reponse. */
export interface PublicQuestion {
  id: string;
  index: number;
  total: number;
  difficulty: Difficulty;
  question: string;
  options: { A: string; B: string; C: string; D: string };
  points: number;
  timeLimit: number;
  deadlineAt: number;
}

export type Letter = "A" | "B" | "C" | "D";

export interface Player {
  id: string;
  name: string;
  gameSlug: string;
  sessionCode: string;
  score: number;
  correctCount: number;
  answeredCount: number;
  status: PlayerStatus;
  startedAt: number;
  finishedAt: number | null;
}

export interface SessionState {
  player: Pick<Player, "name" | "gameSlug" | "score" | "correctCount" | "answeredCount" | "status">;
  game: Game;
  question: PublicQuestion | null;
  finished: boolean;
  position: number;
  totalPlayers: number;
}

export interface AnswerResult {
  correct: boolean;
  correctAnswer: Letter;
  explanation: string;
  gained: number;
  speedBonus: number;
  score: number;
  position: number;
  finished: boolean;
  correctCount: number;
  answeredCount: number;
  total: number;
}

export interface LeaderboardEntry {
  rank: number;
  name: string;
  gameSlug: string;
  score: number;
  status: PlayerStatus;
  correctCount: number;
  answeredCount: number;
}

export interface Stats {
  totalPlayers: number;
  playing: number;
  finished: number;
  waiting: number;
  averageScore: number;
  byGame: { slug: string; name: string; emoji: string; players: number }[];
}
