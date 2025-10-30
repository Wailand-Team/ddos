import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  // stages بسيطة لكن VUS و DURATION ستأتي من المتغيرات عند التشغيل
  // إذا أردت stages متقدمة عدل هنا أو أضف ENV متغيرات.
};

export default function () {
  const target = __ENV.TARGET || 'http://127.0.0.1:8080/';
  const method = (__ENV.METHOD || 'GET').toUpperCase();
  const body   = __ENV.BODY || '';
  const headers = { 'Content-Type': 'application/x-www-form-urlencoded' };

  if (method === 'POST') {
    http.post(target, body, { headers: headers });
  } else {
    http.get(target);
  }

  // تأخير بسيط لمحاكاة سلوك حقيقي
  sleep(Math.random() * 1.5 + 0.5);
}
