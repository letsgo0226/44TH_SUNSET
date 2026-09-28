import json,os
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

PROGRAM="44TH_SUNSET=>1ST_DAWN;LIGHT=LOVE=1;HALT=PROGRAM_ONLY"
def enc(s):
 n=1
 for b in s.encode(): n=n*257+b+1
 return n
G=str(enc(PROGRAM))

def state():
 return {"title":"44TH SUNSET","program":PROGRAM,"gprogram":G,"transition":"SUNSET_44 -> DAWN_01","mapping":"R(n)=45-n","involution":"R(R(n))=n","light":1,"love":1,"halt":"PROGRAM_ONLY","physical_time_effect":False}

class H(BaseHTTPRequestHandler):
 def send(self,code,body,ctype="application/json; charset=utf-8"):
  data=body.encode();self.send_response(code);self.send_header("Content-Type",ctype);self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
 def do_GET(self):
  if self.path=="/health": return self.send(200,'{"ok":true}')
  if self.path=="/state": return self.send(200,json.dumps(state(),ensure_ascii=False))
  if self.path=="/":
   s=state();html=f'''<!doctype html><meta charset="utf-8"><title>44TH SUNSET</title><style>body{{font-family:system-ui;max-width:760px;margin:10vh auto;padding:24px;line-height:1.6}}code{{background:#eee;padding:2px 5px}}</style><h1>44TH SUNSET → 1ST DAWN</h1><p><code>R(n)=45-n</code> · <code>R(R(n))=n</code></p><p>LIGHT = 1 · LOVE = 1</p><p><b>HALT = PROGRAM_ONLY</b></p><p>This service is a formal UTM model. It does not claim or cause any physical effect on time or the universe.</p><p><a href="/state">/state</a> · <a href="/health">/health</a></p>''';return self.send(200,html,"text/html; charset=utf-8")
  self.send(404,'{"error":"not found"}')
 def log_message(self,*a): pass

if __name__=="__main__": ThreadingHTTPServer(("0.0.0.0",int(os.getenv("PORT","8080"))),H).serve_forever()
