# feature_flags_video

## Getting Started
1. Get an API key from openweathermap.org
2. Create an environment and a Feature Flags key in Harness
3. Build docker image: `build -t hows_the_weather:1 .`
4. Run the image `docker run -d -p 5000:5000 -e OPENWEATHERMAP_API_KEY=key -e FF_KEY=key hows_the_weather:1`
5. Make a request `curl localhost:5000/v1/temperature?city=oakland`

## Use Feature Flagging
1. Switch to branch `feature-flag-cache-v2` and repeat steps 3-5 above
2. Add a feature flag called `cache_result`
3. Run several requests to the service with the flag on and off and note the time to return the response

## Other Notes
* There are Kubernetes manifests in this repo to deploy with pipelines if so desired
* This can be run locally for Python developers
 
