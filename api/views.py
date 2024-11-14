from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('ordem')
    serializer_class = TaskSerializer

class TaskUpdateView(APIView):
    def put(self, request, pk):
        try:
            # Obtém a tarefa a ser atualizada e os dados da requisição
            task = Task.objects.get(pk=pk)
            new_order = request.data.get("ordem")

            # Verifica se a nova ordem já está em uso por outra tarefa
            if Task.objects.filter(ordem=new_order).exclude(pk=pk).exists():
                # Ajuste das ordens das tarefas para evitar conflito
                tasks = Task.objects.order_by("ordem")
                
                # Reorganiza as tarefas: mova para baixo as tarefas com ordem maior ou igual à nova ordem
                for t in tasks:
                    if t.ordem >= new_order and t != task:
                        t.ordem += 1  # Aumente a ordem das tarefas subsequentes
                        t.save()

            # Agora, atualize a tarefa com a nova ordem
            task.ordem = new_order
            task.save()

            # Serializa e retorna a resposta
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
