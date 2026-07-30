{{/*
Chart name
*/}}
{{- define "redis-fastapi.name" -}}
redis-fastapi
{{- end }}


{{/*
Full resource name
*/}}
{{- define "redis-fastapi.fullname" -}}
{{ .Release.Name }}-{{ include "redis-fastapi.name" . }}
{{- end }}


{{/*
Common labels
*/}}
{{- define "redis-fastapi.labels" -}}
app.kubernetes.io/name: {{ include "redis-fastapi.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}
