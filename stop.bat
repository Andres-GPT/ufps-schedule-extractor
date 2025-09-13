@echo off
echo Stopping Cloud Run service: ufps-schedule-extractor ...
gcloud run services delete ufps-schedule-extractor --region us-central1 --quiet
echo Service stopped successfully.
pause
