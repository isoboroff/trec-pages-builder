# Proceedings - Video-To-Text 2024

#### TRECVID 2024 - Evaluating video search, captioning, and activity recognition

_George Awad (NIST), Jonathan Fiscus (NIST), Afzal Godil (NIST), Lukas Diduch (NIST), Yvette Graham (Trinity College Dublin), Georges Quénot (LIG)_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_avs.vtt.actev.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_avs.vtt.actev.pdf)
??? abstract "Abstract"
	
	The TREC Video Retrieval Evaluation (TRECVID) is a TREC-style video analysis and retrieval evaluation with the goal of promoting progress in research and development of content-based exploitation and retrieval of information from digital video via open, tasks-based evaluation supported by metrology.
Over the last two decades, this effort has yielded a better understanding of how systems can effectively accomplish such processing and how one can reliably benchmark their performance. TRECVID has been funded by NIST (National Institute of Standards and Technology) and other US government agencies. In addition, many organizations and individuals world-wide contribute significant time and effort. This year TRECVID has been merged back to TREC (Text Retrieval Conference1) and planned the following four tracks:
1. Ad-hoc Video Search (AVS)
2. Video to Text (VTT)
3. Activities in Extended Video (ActEV)
4. Medical Video Question Answering (Med-VidQA)
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-6,
		author = {George Awad (NIST), Jonathan Fiscus (NIST), Afzal Godil (NIST), Lukas Diduch (NIST), Yvette Graham (Trinity College Dublin), Georges Quénot (LIG)},
		title = {TRECVID 2024 - Evaluating video search, captioning, and activity recognition},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {coordinators},
		trec_runs = {},
		trec_tracks = {avs.vtt.actev},
		url = {https://trec.nist.gov/pubs/trec33/papers/Overview_avs.vtt.actev.pdf}
	}
	```

#### softbank-meisei-trec2024-papers-proc-2

_Aiswariya Manoj Kumar（Softbank Corp.）, Hiroki Takushima（Softbank Corp.）, Yuma Suzuki（Softbank Corp.）, Hayato Tanoue（Softbank Corp.）, Hiroki Nishihara（Softbank Corp.）, Yuki Shibata（Softbank Corp.）, Haruki Sato（Agoop Corp.）, Takumi Takada（SB Intuitions Corp.）, Takayuki Hori（Softbank Corp.）, Kazuya Ueki（Meisei Univ.）_

- :fontawesome-solid-user-group: **Participant:** [softbank-meisei](./participants.md#softbank-meisei)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.rag.pdf)
- :material-file-search: **Runs:** [SoftbankMeisei_vtt_main_run1](./runs.md#softbankmeisei_vtt_main_run1) | [SoftbankMeisei_vtt_main_run2](./runs.md#softbankmeisei_vtt_main_run2) | [SoftbankMeisei_vtt_main_run3](./runs.md#softbankmeisei_vtt_main_run3) | [SoftbankMeisei_vtt_main_run4](./runs.md#softbankmeisei_vtt_main_run4) | [SoftbankMeisei_vtt_sub_run2](./runs.md#softbankmeisei_vtt_sub_run2) | [SoftbankMeisei_vtt_sub_run3](./runs.md#softbankmeisei_vtt_sub_run3) | [SoftbankMeisei_vtt_sub_run1](./runs.md#softbankmeisei_vtt_sub_run1)

??? abstract "Abstract"
	
	The Softbank-Meisei team participated in the ad-hoc video search (AVS) and video-to-text (VTT) tasks at TREC 2024. In this year's AVS task, we submitted four fully automatic systems for both the main and progress tasks. Our systems utilized pre-trained vision and language models, including CLIP, BLIP, and BLIP-2, along with several other advanced models. We also expanded the original query texts using text generation and image generation techniques to enhance data diversity. The integration ratios of these models were optimized based on results from previous benchmark test datasets. In this year's VTT, as last year, we submitted four main task methods using multiple model captioning, reranking, and generative AI for summarization. For the subtasks, we submitted three methods using the output of each model. Last year's test data for the main task showed improvements of about 0.04 points in CIDEr-D and about 0.03 points in SPICE, based on the indices we had on hand.
	

??? quote "Bibtex"
	```
	@inproceedings{softbank-meisei-trec2024-papers-proc-2,
		author = {Aiswariya Manoj Kumar（Softbank Corp.）, Hiroki Takushima（Softbank Corp.）, Yuma Suzuki（Softbank Corp.）, Hayato Tanoue（Softbank Corp.）, Hiroki Nishihara（Softbank Corp.）, Yuki Shibata（Softbank Corp.）, Haruki Sato（Agoop Corp.）, Takumi Takada（SB Intuitions Corp.）, Takayuki Hori（Softbank Corp.）, Kazuya Ueki（Meisei Univ.）},
		title = {softbank-meisei-trec2024-papers-proc-2},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {softbank-meisei},
		trec_runs = {rtask-bm25-colbert_faiss, rtask-bm25-rank_zephyr, rag_bm25-colbert_faiss-gpt4o-llama70b, ragtask-bm25-rank_zephyr-gpt4o-llama70b, agtask-bm25-colbert_faiss-gpt4o-llama70b},
		trec_tracks = {rag},
		url = {https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.rag.pdf}
	}
	```

#### Softbank-Meisei at TREC 2024 Ad-hoc Video Search and Video to Text Tasks

_Kazuya Ueki (Meisei University), Yuma Suzuki (SoftBank Corp.), Hiroki Takushima (SoftBank Corp.), Haruki Sato (Agoop Corp.), Takumi Takada (SB Intuitions Corp.), Aiswariya Manoj Kumar (SoftBank Corp.), Hayato Tanoue (SoftBank Corp.), Hiroki Nishihara (SoftBank Corp.), Yuki Shibata (SoftBank Corp.), Takayuki Hori (SoftBank Corp.)_

- :fontawesome-solid-user-group: **Participant:** [softbank-meisei](./participants.md#softbank-meisei)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.avs.vtt.pdf](https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.avs.vtt.pdf)
- :material-file-search: **Runs:** [SoftbankMeisei_vtt_main_run1](./runs.md#softbankmeisei_vtt_main_run1) | [SoftbankMeisei_vtt_main_run2](./runs.md#softbankmeisei_vtt_main_run2) | [SoftbankMeisei_vtt_main_run3](./runs.md#softbankmeisei_vtt_main_run3) | [SoftbankMeisei_vtt_main_run4](./runs.md#softbankmeisei_vtt_main_run4) | [SoftbankMeisei_vtt_sub_run2](./runs.md#softbankmeisei_vtt_sub_run2) | [SoftbankMeisei_vtt_sub_run3](./runs.md#softbankmeisei_vtt_sub_run3) | [SoftbankMeisei_vtt_sub_run1](./runs.md#softbankmeisei_vtt_sub_run1)

??? abstract "Abstract"
	
	The Softbank-Meisei team participated in the ad-hoc video search (AVS) and video-to-text (VTT) tasks at TREC 2024. In this year's AVS task, we submitted four fully automatic systems for both the main and progress tasks. Our systems utilized pre-trained vision and language models, including CLIP, BLIP, and BLIP-2, along with several other advanced models. We also expanded the original query texts using text generation and image generation techniques to enhance data diversity. The integration ratios of these models were optimized based on results from previous benchmark test datasets. In this year's VTT, as last year, we submitted four main task methods using multiple model captioning, reranking, and generative AI for summarization. For the subtasks, we submitted three methods using the output of each model. Last year's test data for the main task showed improvements of about 0.04 points in CIDEr-D and about 0.03 points in SPICE, based on the indices we had on hand.
	

??? quote "Bibtex"
	```
	@inproceedings{softbank-meisei-trec2024-papers-proc-3,
		author = {Kazuya Ueki (Meisei University), Yuma Suzuki (SoftBank Corp.), Hiroki Takushima (SoftBank Corp.), Haruki Sato (Agoop Corp.), Takumi Takada (SB Intuitions Corp.), Aiswariya Manoj Kumar (SoftBank Corp.), Hayato Tanoue (SoftBank Corp.), Hiroki Nishihara (SoftBank Corp.), Yuki Shibata (SoftBank Corp.), Takayuki Hori (SoftBank Corp.)},
		title = {Softbank-Meisei at TREC 2024 Ad-hoc Video Search and Video to Text Tasks},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {softbank-meisei},
		trec_runs = {SoftbankMeisei - Progress Run 1, SoftbankMeisei - Progress Run 2, SoftbankMeisei - Progress Run 3, SoftbankMeisei - Progress Run 4, SoftbankMeisei - Main Run 1, SoftbankMeisei - Main Run 2, SoftbankMeisei - Main Run 3, SoftbankMeisei - Main Run 4, SoftbankMeisei_vtt_main_run1, SoftbankMeisei_vtt_main_run2, SoftbankMeisei_vtt_main_run3, SoftbankMeisei_vtt_main_run4, SoftbankMeisei_vtt_sub_run2, SoftbankMeisei_vtt_sub_run3, SoftbankMeisei_vtt_sub_run1},
		trec_tracks = {avs.vtt},
		url = {https://trec.nist.gov/pubs/trec33/papers/softbank-meisei.avs.vtt.pdf}
	}
	```

