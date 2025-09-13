@echo off
echo Starting Cloud Run service: ufps-schedule-extractor ...
gcloud run deploy ufps-schedule-extractor ^
  --image gcr.io/ufps-schedule/ufps-schedule-extractor ^
  --platform managed ^
  --region us-central1 ^
  --allow-unauthenticated
echo Service deployed successfully.
pause
