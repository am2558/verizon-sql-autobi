start-backend:
	cd backend && python app.py

start-frontend:
	cd frontend && python fletty.py

start:
	make -j2 start-backend start-frontend
