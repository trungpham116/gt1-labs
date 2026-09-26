import { createRequire } from 'node:module';
import { readdir } from 'node:fs/promises';
import { join } from 'node:path';

const require = createRequire(import.meta.url);
const sharp = require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');

const folder = new URL('./qr/', import.meta.url).pathname;
for (const name of await readdir(folder)) {
  if (!name.endsWith('.svg')) continue;
  await sharp(join(folder, name), { density: 300 })
    .flatten({ background: '#ffffff' })
    .resize(720, 720, { kernel: 'nearest' })
    .png()
    .toFile(join(folder, name.replace('.svg', '.png')));
}
