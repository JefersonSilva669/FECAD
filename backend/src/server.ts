import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import http from 'http';
import { Server } from 'socket.io';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: '*',
  }
});

// Websockets chat logic
io.on('connection', (socket) => {
  console.log('Um usuário conectou:', socket.id);

  socket.on('join_subject_chat', (subjectId: string) => {
    socket.join(`room_${subjectId}`);
    console.log(`Socket ${socket.id} entrou na sala room_${subjectId}`);
  });

  socket.on('send_message', (data: { subjectId: string, userId: string, content: string }) => {
    // Aqui no futuro chamaremos o Prisma para salvar no PostgreSQL:
    // await prisma.message.create(...)

    // Enviar mensagem para todos na sala
    io.to(`room_${data.subjectId}`).emit('new_message', data);
  });

  socket.on('disconnect', () => {
    console.log('Usuário desconectou:', socket.id);
  });
});

// Rotas REST Básicas (Exemplo)
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'Backend do FECAD está rodando!' });
});

const PORT = process.env.PORT || 3333;
server.listen(PORT, () => {
  console.log(`🚀 Servidor rodando na porta ${PORT}`);
});
