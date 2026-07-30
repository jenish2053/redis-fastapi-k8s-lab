from fastapi import FastAPI, HTTPException
import redis
import os

app = FastAPI(title="Redis FastAPI Demo")


# Redis configuration from Kubernetes environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")


try:
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )

except Exception:
    redis_client = None


@app.get("/")
def root():
    return {
        "message": "Welcome to Redis + FastAPI!",
        "redis_host": REDIS_HOST
    }


@app.get("/health")
def health():
    try:
        redis_client.ping()

        return {
            "status": "healthy",
            "redis": "connected"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Redis connection failed: {e}"
        )


@app.post("/set/{key}/{value}")
def set_value(key: str, value: str):
    try:
        redis_client.set(key, value)

        return {
            "message": f"Stored '{value}' with key '{key}'"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/get/{key}")
def get_value(key: str):
    try:
        value = redis_client.get(key)

        if value is None:
            raise HTTPException(
                status_code=404,
                detail="Key not found"
            )

        return {
            "key": key,
            "value": value
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
