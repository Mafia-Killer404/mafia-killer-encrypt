import marshal, base64
exec(marshal.loads(base64.b64decode("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")))