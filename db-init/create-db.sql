CREATE TABLE IF NOT EXISTS public.works
(
    id serial NOT NULL PRIMARY KEY,
    user_id bigint NOT NULL,
    file_id character varying(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.votes
(
    id serial NOT NULL PRIMARY KEY,
    user_id bigint NOT NULL,
    work_id integer NOT NULL,
    grade integer NOT NULL,
    CONSTRAINT votes_work_id_fkey FOREIGN KEY (work_id)
        REFERENCES public.works (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
