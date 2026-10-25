"""Exporter smoke and failure tests: python3 -m unittest discover -s tests."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from export_manuscript import export


class ExportTests(unittest.TestCase):
    def test_scene_only_and_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scenes = root / "40 Books" / "Test" / "Scenes"
            scenes.mkdir(parents=True)
            (scenes / "001.md").write_text("---\nstatus: working\n---\n## Plán\nTajný plán\n## Text\nPrvní scéna.\n## Poznámky\nTajná poznámka\n", encoding="utf-8")
            (scenes / "002.md").write_text("## Text\nDruhá scéna.\n", encoding="utf-8")
            manuscript = scenes.parent / "Manuscript.md"
            manuscript.write_text("---\ntype: manuscript\n---\n# Kniha\n\n![[Scenes/002#Text]]\n\n![[Scenes/001#Text]]\n", encoding="utf-8")
            result = export(manuscript, root)
            self.assertIn("Druhá scéna.\n\nPrvní scéna.", result)
            self.assertNotIn("Tajný plán", result)
            self.assertNotIn("Tajná poznámka", result)
            self.assertNotIn("status:", result)

    def test_missing_scene_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manuscript = root / "Manuscript.md"
            manuscript.write_text("![[Missing#Text]]", encoding="utf-8")
            with self.assertRaises(ValueError):
                export(manuscript, root)

    def test_invalid_embed_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manuscript = root / "Manuscript.md"
            manuscript.write_text("![[Scene]]", encoding="utf-8")
            with self.assertRaises(ValueError):
                export(manuscript, root)


if __name__ == "__main__":
    unittest.main()
