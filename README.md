# Energy Watch
Oversikt over energikomponenter

## Implementerte deler
Jeg valgte å implementere backend og frontend funksjonalitet. Testing kun opprettet malen.

**Backend**
- REST-API for å opprette, liste, hente, oppdatere og slette komponenter
- Validering av navn, status og type, med feilmeldinger ved ugyldige data
- Lagring i SQLite, slik at data beholdes etter omstart

**Frontend**
- Oversikt over alle komponenter
- Skjema for å legge til nye komponenter
- Knapp for å slette komponenter

## Forutsetninger
- Python 3.14 eller nyere
- `backend/requirements.txt`.

## Kjøre løsningen
1. Gå til backend-mappa og opprett et virtuelt miljø:
   ```bash
   cd backend
   python -m venv .venv
   ```

2. Aktiver det virtuelle miljøet:
   ```bash
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # macOS/Linux
   source .venv/bin/activate
   ```

3. Installer avhengighetene:
   ```bash
   pip install -r requirements.txt
   ```

4. Start serveren:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Åpne løsningen i nettleseren:
- API: http://localhost:8000/api/components
- Frontend: http://localhost:8000/app
- Api-test: ```bash python -m pytest```

6. Test API-et (forutsetter at serveren kjører, bytt X med en int id som finnes) via Powershell:
- Hent alle: Invoke-RestMethod http://127.0.0.1:8000/api/components
- Hent én: Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/api/components/X
- Opprett: Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/components -ContentType "application/json" -Body '{"name": "Something ...", "status": "active", "type": "transformator"}'
- Oppdater: Invoke-RestMethod -Method Put -Uri http://127.0.0.1:8000/api/components/X -ContentType "application/json" -Body '{"name": "Something ...", "status": "maintenance", "type": "battery"}'
- Slett: Invoke-RestMethod -Method Delete -Uri http://127.0.0.1:8000/api/components/X


## Teknologivalg
- Backend: Python og FastAPI for lite oppsett og innebygd API-dokumentasjon
- Database: Sqlite
- Frontend: HTML, CSS og JavaScript
- Testing: pytest

## Struktur
Backend:
- `main.py` tar imot forespørsler og sender svar tilbake.
- `validation.py` sjekker at dataene er gyldige.
- `repository.py` inneholder SQL-spørringene som leser og lagrer data.
- `database.py` kobler til databasen og oppretter tabellen.

Frontend:
- `index.html` sidens innhold.
- `style.css` - styling av siden.
- `script.js` henter, legger til og sletter komponenter via backend + oppdaterer siden.
